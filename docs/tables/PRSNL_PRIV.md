# PRSNL_PRIV

> This table is used to store the privileges to maintain the personnel.

**Description:** Personnel privileges.  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_PRIV_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `NAME` | VARCHAR(50) | NOT NULL |  | The name of the privilege. This needs to be unique for a given personnel_id |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person ID for the person for whom this privilege row is maintained |
| 9 | `PRSNL_PRIV_ID` | DOUBLE | NOT NULL | PK | The unique ID of the Personnel Privilege record on the table |
| 10 | `SUPER_USER_IND` | DOUBLE | NOT NULL |  | Indicates whether the user referenced by the personnel_id has super user privileges I.e. can maintain any position, organization etc. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `USE_ORG_RELTN_IND` | DOUBLE | NOT NULL |  | Indicates whether the users org relationship needs to be used for the privilege |
| 17 | `USE_POSITION_IND` | DOUBLE | NOT NULL |  | Indicates whether the users position needs to be used for the privilege |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PRSNL_PRIV_COMPONENT](PRSNL_PRIV_COMPONENT.md) | `PRSNL_PRIV_ID` |
| [PRSNL_PRIV_DETAIL](PRSNL_PRIV_DETAIL.md) | `PRSNL_PRIV_ID` |

