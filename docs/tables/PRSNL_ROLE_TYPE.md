# PRSNL_ROLE_TYPE

> stores prsnl role type relation information

**Description:** prsnl role type  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_ROLE_TYPE_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who created the request. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL |  | PERSON identifier |
| 10 | `PREV_PRSNL_ROLE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies a previous version of a personnel role type |
| 11 | `PRSNL_ROLE_TYPE_ID` | DOUBLE | NOT NULL | PK | personnel role type identifier |
| 12 | `ROLE_BEG_DT_TM` | DATETIME |  |  | Date stamp of when the role is/was effective. |
| 13 | `ROLE_END_DT_TM` | DATETIME |  |  | Date stamp of when the role is/was ended. |
| 14 | `ROLE_TYPE_RELTN_ID` | DOUBLE | NOT NULL | FK→ | role type relation identifier |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_PRSNL_ROLE_TYPE_ID` | [PRSNL_ROLE_TYPE](PRSNL_ROLE_TYPE.md) | `PRSNL_ROLE_TYPE_ID` |
| `ROLE_TYPE_RELTN_ID` | [ROLE_TYPE_RELTN](ROLE_TYPE_RELTN.md) | `ROLE_TYPE_RELTN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PRSNL_ROLE_TYPE](PRSNL_ROLE_TYPE.md) | `PREV_PRSNL_ROLE_TYPE_ID` |
| [PRSNL_ROLE_TYPE_RESP](PRSNL_ROLE_TYPE_RESP.md) | `PRSNL_ROLE_TYPE_ID` |

