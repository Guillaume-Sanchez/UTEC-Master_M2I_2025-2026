export let level1 = [
    {
        id: 1,
        hash: "48bb6e862e54f2a795ffc4e541caed4d",
        response: "easy",
        help: "md5",
    },
    {
        id: 2,
        hash: "CBFDAC6008F9CAB4083784CBD1874F76618D2A97 ",
        response: "password123",
        help: "sha.. but which version",
    },
    {
        id: 3,
        hash: "1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032",
        response: "letmein",
        help: "sha..",
    },
    {
        id: 4,
        hash: "$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom",
        response: "bleh",
        help: "Search the hashcat examples page (https://hashcat.net/wiki/doku.php?id=example_hashes) for $2y$. This type of hash can take a very long time to crack, so either filter rockyou for four character words, or use a mask for four lower case alphabetical characters.",
    },
    {
        id: 5,
        hash: "279412f945939ba78ce0758d3fd83daa",
        response: "Eternity22",
        help: "md4",
    }
];

export let level2 = [
    {
        id: 6,
        hash: "Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85",
        response: "paule",
        help: "md5",
    },
    {
        id: 7,
        hash: "Hash: 1DFECA0C002AE40B8619ECF94819CC1B ",
        response: "n63umy8lkf4i",
        help: "sha.. but which version",
    },
    {
        id: 8,
        hash: "Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.",
        response: "waka99",
        help: "Salt: aReallyHardSalt",
    },
    {
        id: 9,
        hash: "Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6",
        response: "481616481616",
        help: "Salt: tryhackme",
    },
];
