# OAF_PROFILE

> The profile table contains profiles required by an insurance company which are used to contact the third party to obtain information regarding ones insurance coverage.

**Description:** profile  
**Table type:** ACTIVITY  
**Primary key:** `PROFILE_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT` | DATETIME |  |  | Date the profile was created |
| 6 | `CONTACT_NAME` | VARCHAR(50) |  |  | Contact name |
| 7 | `END_EFFECTIVE_DT` | DATETIME |  |  | Date the profile expires |
| 8 | `LOGON_ID` | VARCHAR(8) |  |  | Logon id |
| 9 | `NEW_PASSWORD` | VARCHAR(10) |  |  | New password |
| 10 | `OLD_PASSWORD` | VARCHAR(10) |  |  | Old password |
| 11 | `PROFILE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the oaf_profile table. It is an internal system assigned number. |
| 12 | `PROFILE_NAME` | VARCHAR(20) |  |  | Profile name |
| 13 | `PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | Profile_type_cd (whether request or reply) |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OAF_PROFILE_DETAIL](OAF_PROFILE_DETAIL.md) | `PROFILE_ID` |

