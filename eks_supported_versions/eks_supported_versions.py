import urllib.request

AWS_EKS_DOCS_LINK = "https://raw.githubusercontent.com/awsdocs/amazon-eks-user-guide/master/doc_source/kubernetes-versions.md"
KUBERNETES_VERSIONS_STARTER_LINE = "The following Kubernetes versions are currently available for new Amazon EKS clusters:\n"
KUBERNETES_VERSIONS_CALENDAR_STARTER_LINE = "| Kubernetes version | Upstream release | Amazon EKS release | Amazon EKS end of support | \n"


def get_raw_lines_from_github():
    f = urllib.request.urlopen(AWS_EKS_DOCS_LINK)
    return f.readlines()


def get_supported_eks_versions():
    """
    get_supported_eks_versions
    """

    lines = get_raw_lines_from_github()

    start = -1
    for count, line in enumerate(lines):
        if line.decode("utf-8") == KUBERNETES_VERSIONS_STARTER_LINE:
            start = count
            break

    if start == -1:
        raise Exception("NotFound", "Could not find Supported eks versions")

    start += 1
    versions = []

    while True:
        line = lines[start].decode("utf-8")
        if line[0] != "+":
            break

        line = line.strip()
        line = line.replace("\\", "")
        line = line.replace("+ ", "")

        versions.append(line)
        start += 1

    return versions


def get_supported_eks_versions_calendar():
    """
    get_supported_eks_versions_calendar
    """

    lines = get_raw_lines_from_github()

    start = -1
    for count, line in enumerate(lines):
        if line.decode("utf-8") == KUBERNETES_VERSIONS_CALENDAR_STARTER_LINE:
            start = count
            break

    if start == -1:
        raise Exception("NotFound", "Could not find Supported eks versions")

    start += 2
    line = lines[start].decode("utf-8")

    versions = []

    while True:
        line = lines[start].decode("utf-8")
        if line[0] != "|":
            break

        split_line = line.split("|")
        current = {}
        current["kubernetes_version"] = split_line[1].strip().replace("\\", "")
        current["upstream_release"] = split_line[2].strip()
        current["amazon_eks_release"] = split_line[3].strip()
        current["amazon_eks_end_of_support"] = split_line[4].strip()
        versions.append(current)
        start += 1

    return versions
