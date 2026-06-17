# OMF_AUTH_PRSNL_GROUP

> The authentication value(s) which have been implemented for a specific PRSNL_GROUP.

**Description:** OMF Authorization Personnel Group  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ATTR_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The foreign key from the table that is being checked for authentication values. |
| 3 | `ATTR_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table whose values are being authenticated. |
| 4 | `ATTR_VALUE_TXT` | VARCHAR(255) |  |  | The string value that is implemented for authentication. This is used when the authenticated value is not one stored in a Millennium table. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `OMF_AUTH_LOGON_ATTR_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The internal surrogate value which identifies the logon type and attribute type value(s) associated with this record. |
| 8 | `OMF_AUTH_PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the OMF_AUTH_PRSNL_GROUP table. |
| 9 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The internal surrogate value which identifies the group that is using these particular security validations. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OMF_AUTH_LOGON_ATTR_RELTN_ID` | [OMF_AUTH_LOGON_ATTR_RELTN](OMF_AUTH_LOGON_ATTR_RELTN.md) | `OMF_AUTH_LOGON_ATTR_RELTN_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

