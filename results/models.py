from django.db import models


class State(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.name


class LGA(models.Model):
    lga_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=100)
    state_id = models.IntegerField()

    class Meta:
        db_table = 'lga'

    def __str__(self):
        return self.lga_name


class Ward(models.Model):
    ward_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=100)
    lga_id = models.IntegerField()

    class Meta:
        db_table = 'ward'

    def __str__(self):
        return self.ward_name


class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    polling_unit_name = models.CharField(max_length=255)
    user_ip_address = models.CharField(max_length=50, default='0.0.0.0')

    class Meta:
        db_table = 'polling_unit'

    def __str__(self):
        return self.polling_unit_name


class AnnouncedPUResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation = models.CharField(max_length=10)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'announced_pu_results'

    def __str__(self):
        return f"{self.party_abbreviation} - {self.party_score}"


class AnnouncedLGAResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    party_abbreviation = models.CharField(max_length=10)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'announced_lga_results'

    def __str__(self):
        return f"{self.lga_id} - {self.party_abbreviation} - {self.party_score}"
