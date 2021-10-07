// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Myedgeorder.Outputs
{

    /// <summary>
    /// Specifications of the configurations
    /// </summary>
    [OutputType]
    public sealed class SpecificationResponse
    {
        /// <summary>
        /// Name of the specification
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Value of the specification
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private SpecificationResponse(
            string name,

            string value)
        {
            Name = name;
            Value = value;
        }
    }
}
