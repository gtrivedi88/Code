RHTAP enables developers to containerize and deploy their applications in a matter of minutes. And it creates a build pipeline that allows developers to test potential changes to those applications, and quickly integrate the changes once they are verified. Perhaps best of all, RHTAP further provides rigorous security against supply-chain attacks. It conforms to the most demanding requirements of the Supply chain Levels for Software Artifacts (SLSA) security framework.

But before developers in your organization can leverage any of these benefits, you must install Red Hat Trusted Application Pipeline. This document explains how to complete that process.

To install RHTAP, you must complete five procedures:
Creating a GitHub application
Forking the template catalog and cloning the install repo
Creating a private-values.yaml file
Installing RHTAP in your chosen cluster
Accessing RHTAP for the first time

The following pages of this document explain each of those procedures in detail. Before you can begin, however, you must ensure you have the following prerequisites:
ClusterAdmin access to an OpenShift Container Platform (OCP) cluster, through both the CLI and the web console
An instance of Red Hat Advanced Cluster Security 
The Helm CLI tool
A GitHub account
Once you have these prerequisites, you are ready to start the installation process by creating a new GitHub application for your instance of RHTAP.
