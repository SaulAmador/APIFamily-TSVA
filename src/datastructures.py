"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # initialize with three members as per instructions
        self._members = []

        # first member
        self._members.append({
            "id": self._generate_id(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })

        # second member
        self._members.append({
            "id": self._generate_id(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })

        # third member
        self._members.append({
            "id": self._generate_id(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        })

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        """Add a new member to the family.

        The provided ``member`` dict may or may not contain an ``id`` or
        ``last_name``.  This method will:

        1. Assign a unique identifier if none is provided (or if ``None``).
        2. Ensure ``last_name`` is set to the family's last name.
        3. Update the internal ``_next_id`` counter if a manual id is
           supplied and is greater than the current value.
        4. Append the normalized member to ``self._members`` and return it.
        """
        # generate an id if necessary
        if "id" not in member or member.get("id") is None:
            member["id"] = self._generate_id()
        else:
            # ensure our counter stays ahead
            try:
                provided = int(member["id"])
                if provided >= self._next_id:
                    self._next_id = provided + 1
            except Exception:
                # ignore non-int id, let it raise later if needed
                pass

        # last name always matches the family
        member["last_name"] = self.last_name

        self._members.append(member)
        return member

    def delete_member(self, id):
        """Remove a member with the given ``id``.

        Returns ``True`` if a member was deleted, ``False`` otherwise.
        """
        for index, member in enumerate(self._members):
            if member.get("id") == id:
                del self._members[index]
                return True
        return False

    def get_member(self, id):
        """Return the member dict whose ``id`` matches or ``None`` if missing."""
        for member in self._members:
            if member.get("id") == id:
                return member
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members