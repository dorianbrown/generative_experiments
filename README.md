# Experimenting with generative art

These posts will be heavily inspired by the work of Anders Hoff, which has done some really interesting things on using simple rules to create emergent art. Besides sharing is work and the [code he uses to generate them](https://github.com/inconvergent), he also writes about his process and how he creates what he does on [his website](https://inconvergent.net).

I feel the need to clearly cite him, as most of what I'll be doing here is copying from his work as a starting point.

## Usage

Although you're free to use anything shared here, beware that this won't be very well maintained. I hope to eventually write a library (which will be maintained) for creating stuff like this, but that's still a ways off.

I've found that using pycairo+gtk3 require lots of dependencies outside of python, so I've provided a conda `environment.yml` file. Check [this](https://conda.io/docs/user-guide/tasks/manage-environments.html#sharing-an-environment) out for how to use it. 

I'm running Ubuntu 18.04, so your mileage on other systems may vary.
