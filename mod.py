$ chmod +x ./build.sh
$ ./build.sh -b $CI_COMMIT_REF_NAME
Building titles/about/master.adoc into titles-generated/main/about ...
  asciidoctor --backend=html5 -o index.html --section-numbers -a toc --failure-level ERROR --trace --warnings --destination-dir titles-generated/main/about titles/about/master.adoc
    titles-generated/main/about/index.html
Building titles/install/master.adoc into titles-generated/main/install ...
  asciidoctor --backend=html5 -o index.html --section-numbers -a toc --failure-level ERROR --trace --warnings --destination-dir titles-generated/main/install titles/install/master.adoc
    titles-generated/main/install/index.html
Building titles/managing_ec/master.adoc into titles-generated/main/managing_ec ...
  asciidoctor --backend=html5 -o index.html --section-numbers -a toc --failure-level ERROR --trace --warnings --destination-dir titles-generated/main/managing_ec titles/managing_ec/master.adoc
    titles-generated/main/managing_ec/index.html
Building titles/managing_sboms/master.adoc into titles-generated/main/managing_sboms ...
  asciidoctor --backend=html5 -o index.html --section-numbers -a toc --failure-level ERROR --trace --warnings --destination-dir titles-generated/main/managing_sboms titles/managing_sboms/master.adoc
    titles-generated/main/managing_sboms/index.html
Building titles/release_notes/master.adoc into titles-generated/main/release_notes ...
  asciidoctor --backend=html5 -o index.html --section-numbers -a toc --failure-level ERROR --trace --warnings --destination-dir titles-generated/main/release_notes titles/release_notes/master.adoc
    titles-generated/main/release_notes/index.html
Building titles/software_templates/master.adoc into titles-generated/main/software_templates ...
  asciidoctor --backend=html5 -o index.html --section-numbers -a toc --failure-level ERROR --trace --warnings --destination-dir titles-generated/main/software_templates titles/software_templates/master.adoc
    titles-generated/main/software_templates/index.html
$ mv titles-generated/ public/
Uploading artifacts for successful job
00:02
Uploading artifacts...
public: found 15 matching artifact files and directories 
Uploading artifacts as "archive" to coordinator... 201 Created  id=20604966 responseStatus=201 Created token=64_PtsfV
Cleaning up project directory and file based variables
00:00
Job succeeded
