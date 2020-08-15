"""Test the ``pawian`` namespace added to the ``pandas.DataFrame``"""

from os.path import dirname, realpath

import numpy as np

import pandas as pd

import pytest

import pawian
from pawian.data import create_skeleton_frame, read_ascii


PAWIAN_DIR = dirname(realpath(pawian.__file__))
SAMPLE_DIR = f"{PAWIAN_DIR}/samples"
INPUT_FILE_DATA = f"{SAMPLE_DIR}/momentum_tuples_data.dat"
INPUT_FILE_MC = f"{SAMPLE_DIR}/momentum_tuples_mc.dat"


@pytest.mark.parametrize(
    "particles,number_of_rows",
    [
        (["pi+", "D0", "D-"], 100),
        # (['gamma', 'pi+', 'pi-'], None),
        (None, 50),
    ],
)
def test_create_skeleton(particles, number_of_rows):
    """Test creating an empty pawian dataframe"""
    frame = create_skeleton_frame(
        particle_names=particles, number_of_rows=number_of_rows,
    )
    if number_of_rows is None:
        number_of_rows = 0
    assert not frame.pawian.has_weights
    assert len(frame) == number_of_rows
    if frame.pawian.has_particles:
        assert frame.pawian.particles == particles


@pytest.mark.parametrize(
    "columns,names",
    [
        (  # wrong number of column LEVELS
            [("A"), ("B"), ("C"),],
            ["Particles"],
        ),
        (  # wrong momentum labels
            [("A", "px"), ("A", "b"), ("B", "px"), ("B", "b"),],
            ["Particles", "Momentum"],
        ),
    ],
)
def test_raise_validate(columns, names):
    """Test exception upon validate"""
    multi_index = pd.MultiIndex.from_tuples(columns, names=names)
    frame = pd.DataFrame(columns=multi_index)
    with pytest.raises(AttributeError):
        print(frame.pawian)


def test_properties_multicolumn():
    """Test whether properties work for multicolumn dataframe"""
    particles = ["pi+", "D0", "D-"]
    frame_data = read_ascii(INPUT_FILE_DATA, particles=particles)
    frame_mc = read_ascii(INPUT_FILE_MC, particles=particles)

    assert frame_data.pawian.has_weights
    assert not frame_mc.pawian.has_weights
    with pytest.raises(Exception):
        assert frame_mc.pawian.weights

    assert frame_data.pawian.weights.iloc[1] == 0.990748
    assert frame_data.pawian.weights.iloc[-1] == 0.986252
    assert frame_data.pawian.weights.equals(frame_data.pawian.intensities)

    assert frame_mc.pawian.particles == particles
    assert frame_data.pawian.particles == particles

    momentum_labels = ["p_x", "p_y", "p_z", "E"]
    assert frame_mc.pawian.momentum_labels == momentum_labels
    assert frame_data.pawian.momentum_labels == momentum_labels

    assert np.allclose(
        frame_data.pawian.mass.mean().tolist(),
        [0.13957, 1.86484, 1.86961,],
        atol=1e-5,
    )
    assert np.allclose(
        frame_data.pawian.rho.mean().tolist(),
        [0.14209, 0.64765, 0.69154,],
        atol=1e-5,
    )


def test_properties_single_column():
    """Test whether properties work for single column dataframe"""
    particles = ["pi+", "D0", "D-"]
    pi_data = read_ascii(INPUT_FILE_DATA, particles=particles)["pi+"]
    pi_mc = read_ascii(INPUT_FILE_MC, particles=particles)["pi+"]

    assert pi_data.pawian.energy.iloc[-1] == 0.152749
    assert pi_mc.pawian.energy.iloc[-1] == 0.257006

    assert pi_data.pawian.rho2.iloc[-1] == 0.0038524700603599993

    with pytest.raises(Exception):
        assert pi_data.pawian.particles