# PRSNL_ROLE_PROFILE_ADDN

> This table stores area of work, work groups & business functions for a personnel's role profile.

**Description:** Personnel Role Profile Addition  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHILD_TYPE_CD` | DOUBLE | NOT NULL |  | The type of additional profile information being stored. (e.g. area of work, work gorups, business function) |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PRSNL_ORG_RELTN_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to table PRSNL_ORG_RELTN_TYPE. |
| 9 | `PRSNL_ROLE_PROFILE_ADDN_ID` | DOUBLE | NOT NULL |  | The primary identifier for this table. |
| 10 | `TYPE_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier of the entity that is getting related to the Prsnl_Role_Profile_Addn row. |
| 11 | `TYPE_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table that the value for Type Entity Name is from. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ORG_RELTN_TYPE_ID` | [PRSNL_ORG_RELTN_TYPE](PRSNL_ORG_RELTN_TYPE.md) | `PRSNL_ORG_RELTN_TYPE_ID` |

