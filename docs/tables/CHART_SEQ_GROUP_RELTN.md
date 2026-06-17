# CHART_SEQ_GROUP_RELTN

> For a given group, this table stores the selected items related to the group. If the group type is 'provider', then this table stores the assigned providers to a group. Likewise if the group type is 'organization', then this table stores the assigned organizations.

**Description:** Chart sequence group relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `GROUP_RELTN_ID` | DOUBLE | NOT NULL |  | A number that uniquely identifies a row on this table. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Stores the Location code added to the route stop. Value comes from LOCATION.LOCATION_CD |
| 7 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The unique number associated with a specified organization. |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The unique number associated with a specified provider. |
| 9 | `SEQUENCE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The unique number associated with a specified CHART Sequence Group. |
| 10 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The assigned sequence number to the provider or organization within a group |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SEQUENCE_GROUP_ID` | [CHART_SEQUENCE_GROUP](CHART_SEQUENCE_GROUP.md) | `SEQUENCE_GROUP_ID` |

