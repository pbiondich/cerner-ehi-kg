# OMF_AUTH_LOGON_TYPE

> The logon types which may be used to authorize a user. For example, role-based authority, activity-based authority.

**Description:** OMF Authorization Logon Type  
**Table type:** REFERENCE  
**Primary key:** `OMF_AUTH_LOGON_TYPE_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTH_TYPE_CD` | DOUBLE | NOT NULL |  | The levels of authorization that are available for use. |
| 3 | `LOGON_TYPE_FLAG` | DOUBLE |  |  | The enumerated value, supplied by the HNAM security runtime library, which is associated with this logon type. |
| 4 | `OMF_AUTH_LOGON_TYPE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a row in the OMF_AUTH_LOGON_TYPE table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_AUTH_LOGON_ATTR_RELTN](OMF_AUTH_LOGON_ATTR_RELTN.md) | `OMF_AUTH_LOGON_TYPE_ID` |

