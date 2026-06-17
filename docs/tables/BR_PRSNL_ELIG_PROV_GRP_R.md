# BR_PRSNL_ELIG_PROV_GRP_R

> Stores a group of personnel that are associated to a particular Eligible Provider Group.

**Description:** Bedrock Personnel Eligible Provider Group Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The group that is related to this personnel. |
| 4 | `BR_PRSNL_ELIG_PROV_GRP_R_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_PRSNL_ELIG_PROV_GRP_R table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PRSNL_GROUP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The Personnel Group that this personnel fis related to. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_GROUP_ID` | [BR_GROUP](BR_GROUP.md) | `BR_GROUP_ID` |
| `PRSNL_GROUP_RELTN_ID` | [PRSNL_GROUP_RELTN](PRSNL_GROUP_RELTN.md) | `PRSNL_GROUP_RELTN_ID` |

