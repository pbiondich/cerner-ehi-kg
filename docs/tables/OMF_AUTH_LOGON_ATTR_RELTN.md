# OMF_AUTH_LOGON_ATTR_RELTN

> Relates a logon type (OMF_AUTH_LOGON_TYPE) to the applicable attributes (OMF_AUTH_ATTR).

**Description:** OMF Authorization Logon Attribute Relation  
**Table type:** REFERENCE  
**Primary key:** `OMF_AUTH_LOGON_ATTR_RELTN_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OMF_AUTH_ATTR_ID` | DOUBLE | NOT NULL | FK→ | The attribute that is being associated to the logon type. |
| 2 | `OMF_AUTH_LOGON_ATTR_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a row on the OMF_AUTH_LOGON_ATTR_RELTN table. |
| 3 | `OMF_AUTH_LOGON_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The logon type that is being associated with the given attribute. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OMF_AUTH_ATTR_ID` | [OMF_AUTH_ATTR](OMF_AUTH_ATTR.md) | `OMF_AUTH_ATTR_ID` |
| `OMF_AUTH_LOGON_TYPE_ID` | [OMF_AUTH_LOGON_TYPE](OMF_AUTH_LOGON_TYPE.md) | `OMF_AUTH_LOGON_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_AUTH_PRSNL_GROUP](OMF_AUTH_PRSNL_GROUP.md) | `OMF_AUTH_LOGON_ATTR_RELTN_ID` |

