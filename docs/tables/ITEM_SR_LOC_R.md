# ITEM_SR_LOC_R

> Identifies item exceptions for fill location relationships between an OR and an inventory location

**Description:** Item/Service Resource/Location Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IN_TRANSIT_IND` | DOUBLE |  |  | To store the Intransit status for each Location of corresponding service resource |
| 2 | `ITEM_ID` | DOUBLE | NOT NULL |  | A reference (foreign key) to the item_definition table identifying the item for which an exception exists. |
| 3 | `ITEM_SR_LOC_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of relationship for this item exception, i.e. Surgery Add, Surgery Fill, Surgery Return. These relationships will be queried in Case Pick List Manager when defaulting the list of fill locations that are valid for this item. |
| 4 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The inventory location for which an item exception exists. |
| 5 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence in which to look for "Stored At" locations for the specified item. Used to default a fill location in Case Pick List Manager. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The service resource (CDF Meaning = "SURGOP" -- Surgical Operating Area) for which an item exception is defined. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

