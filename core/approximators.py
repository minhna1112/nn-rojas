import torch
from utils.math import factorial

class PowerLayer(torch.nn.Module):
    def __init__(self, n) -> None:
        super().__init__()
        self.exponents = torch.arange(1, n+1)

    def forward(self, z):
        return torch.pow(z, self.exponents)

class TaylorNetwork(torch.nn.Module):
    def __init__(self, x_0: float, n: int) -> None:
        """
        Args: x_0: The point around which the desired function is approximated
                n: order of derived Taylor series, a.k.a the number of terms used in the series-1, 
                                                   a.k.a the number of hidden Dense layer 
        """
        super().__init__()
        self.x_0 = x_0
        self.n = n
        self.first_layer = torch.nn.Linear(in_features=1, out_features=n, bias=False)
        self.first_layer.weight.requires_grad_(False)
        self.first_layer.weight.fill_(1.0)
        # for w in self.first_layer.parameters():
        #     print(w.size())
        self.power_layer = PowerLayer(n)
        self.last_layer = torch.nn.Linear(in_features=n, out_features=1, bias=True)

    def forward(self, x):
        z = self.first_layer(x - self.x_0) # z  = x - x_0
        z = self.power_layer(z)
        return self.last_layer(z)

    def learn_analytically(self, x, y):
        self.last_layer.bias.requires_grad_(False)
        self.last_layer.bias.fill_
        for i in range(1, self.n+1):
            self.last_layer.weight = ...
        
taylor = TaylorNetwork(x_0=0, n=4)

torch.autograd.grad()