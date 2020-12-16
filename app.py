#!/usr/bin/env python3

from aws_cdk import core

from epsagon_exercise_backend_repo.epsagon_exercise_backend_repo_stack import EpsagonExerciseBackendRepoStack


app = core.App()
EpsagonExerciseBackendRepoStack(app, "epsagon-exercise-backend-repo")

app.synth()
