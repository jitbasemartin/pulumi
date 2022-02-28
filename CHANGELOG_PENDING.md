### Improvements

- [cli/plugins] `pulumi plugin install` can now look up the latest version of plugins on GitHub releases.
  [#9012](https://github.com/pulumi/pulumi/pull/9012)
  
### Bug Fixes

- [sdk/nodejs] - Fix Node `fs.rmdir` DeprecationWarning for Node JS 15.X+
  [#9044](https://github.com/pulumi/pulumi/pull/9044)

- [codegen/go] - Fix secret codegen for input properties
  [#9052](https://github.com/pulumi/pulumi/pull/9052)

- [sdk/nodejs] - `PULUMI_NODEJS_TSCONFIG_PATH` is now explicitly passed to tsnode for the tsconfig file.
  [#9062](https://github.com/pulumi/pulumi/pull/9062)