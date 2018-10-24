# Experimenting with generative art

Here I try and create a set of simple rules for which interact to (hopefully) create interesting emergent patterns. 

<div style="text-align:center">
<img src="examples/random_walks_jumps.svg" width="30%">
</div>

These posts will be heavily inspired by the work of Anders Hoff, which has done some really interesting things in this area. Besides sharing is work and the [code he uses to generate them](https://github.com/inconvergent), he also writes about his process and how he creates what he does on [his website](https://inconvergent.net).

## Usage

Although you're free to use anything shared here, beware that this won't be very well maintained. I hope to eventually write a library (which will be maintained) for creating stuff like this, but that's still a ways off.

Using pycairo+gtk3 requires a lot of dependencies outside of python, so I've provided a conda `environment.yml` file. Check [this](https://conda.io/docs/user-guide/tasks/manage-environments.html#sharing-an-environment) out for how to use it. 

I'm running Ubuntu 18.04, so your mileage on other systems may vary.
