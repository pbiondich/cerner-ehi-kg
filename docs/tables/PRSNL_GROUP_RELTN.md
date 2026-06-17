# PRSNL_GROUP_RELTN

> The personnel group relation table contains pointers to groups which a personnel is included in. Additionally, this table can be used to identify all the personnel in a specific group.

**Description:** Personnel Group Relationship  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_GROUP_RELTN_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 8 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 9 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 12 | `PRIMARY_IND` | DOUBLE |  |  | (Future Use) |
| 13 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the personnel group table. It is an internal system assigned number. |
| 14 | `PRSNL_GROUP_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the personnel group relationship table. It is an internal system assigned number. |
| 15 | `PRSNL_GROUP_R_CD` | DOUBLE | NOT NULL |  | (Future Use). Code set does not exist. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BR_PRSNL_CCN_RELTN](BR_PRSNL_CCN_RELTN.md) | `PRSNL_GROUP_RELTN_ID` |
| [BR_PRSNL_ELIG_PROV_GRP_R](BR_PRSNL_ELIG_PROV_GRP_R.md) | `PRSNL_GROUP_RELTN_ID` |
| [PROXY](PROXY.md) | `GROUP_PROXY_ID` |
| [QMD_PORTAL_PERMISSION](QMD_PORTAL_PERMISSION.md) | `PRSNL_GROUP_RELTN_ID` |
| [TEAM_MEM_PPR_RELTN](TEAM_MEM_PPR_RELTN.md) | `PRSNL_GROUP_RELTN_ID` |

