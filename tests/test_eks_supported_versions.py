import eks_supported_versions


def test_get_supported_eks_versions():
    """
    test_get_supported_eks_versions
    """

    versions = eks_supported_versions.get_supported_eks_versions()
    assert len(versions) == 4

    for version in versions:
        assert version != ""


def test_get_supported_eks_versions_calendar():
    """
    test_get_supported_eks_versions_calendar
    """

    versions = eks_supported_versions.get_supported_eks_versions_calendar()

    for version in versions:
        assert version["kubernetes_version"] is not None
        assert version["kubernetes_version"] != ""

        assert version["upstream_release"] is not None
        assert version["upstream_release"] != ""

        assert version["amazon_eks_release"] is not None
        assert version["amazon_eks_release"] != ""

        assert version["amazon_eks_end_of_support"] is not None
        assert version["amazon_eks_end_of_support"] != ""
