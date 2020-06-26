from abra import Experiment, HypothesisTest
from numpy import median

def test_small_default_bootstrap_ab_test(proportions_data_large):
    exp = Experiment(proportions_data_large, name='proportions-test')

    # run A/B test
    test_ab = HypothesisTest(
        metric='metric',
        control='A', variation='B',
        hypothesis='unequal',
        inference_method='bootstrap'
    )
    results_ab = exp.run_test(test_ab)

    assert results_ab.test_statistic == 'bootstrap-mean-delta'
    assert results_ab.accept_hypothesis


def test_small_default_bootstrap_aa_test(proportions_data_small):
    exp = Experiment(proportions_data_small, name='proportions-test')

    # run A/B test
    test_ab = HypothesisTest(
        metric='metric',
        control='A', variation='A',
        hypothesis='unequal',
        inference_method='bootstrap'
    )
    results_ab = exp.run_test(test_ab)

    assert results_ab.test_statistic == 'bootstrap-mean-delta'
    assert not results_ab.accept_hypothesis

def test_small_median_bootstrap_ab_test(proportions_data_small):
    exp = Experiment(proportions_data_small, name='proportions-test')

    # run A/B test
    test_ab = HypothesisTest(
        metric='metric',
        control='A', variation='D',
        hypothesis='unequal',
        inference_method='bootstrap',
        statistic_function=median,
    )
    results_ab = exp.run_test(test_ab)

    assert results_ab.test_statistic == 'bootstrap-median-delta'
    assert results_ab.accept_hypothesis


def test_small_median_bootstrap_aa_test(proportions_data_small):
    exp = Experiment(proportions_data_small, name='proportions-test')

    # run A/B test
    test_ab = HypothesisTest(
        metric='metric',
        control='A', variation='A',
        hypothesis='unequal',
        inference_method='bootstrap',
        statistic_function=median,
    )
    results_ab = exp.run_test(test_ab)

    assert results_ab.test_statistic == 'bootstrap-median-delta'
    assert not results_ab.accept_hypothesis