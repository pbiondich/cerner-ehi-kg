# OMF_AUTH_ATTR

> The security attributes which may be implemented for a given logon type. For example, Organization or Application Group.

**Description:** OMF Authorization Attribute  
**Table type:** REFERENCE  
**Primary key:** `OMF_AUTH_ATTR_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTR_CD` | DOUBLE | NOT NULL |  | The characteristic that will be used for authorization requirements. |
| 2 | `ATTR_DATA_TYPE_FLAG` | DOUBLE |  |  | The data type associated with this attribute. |
| 3 | `FILTER_MEANING` | VARCHAR(50) | NOT NULL | FK→ | Generic character representation of this particular attribute. |
| 4 | `OMF_AUTH_ATTR_ID` | DOUBLE | NOT NULL | PK | Unique, generated number to identify a single row in the OMF_AUTH_ATTR table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VAL1` | VARCHAR(255) |  |  | Passed in string value 1 to filter scripts. Typically will be the filter program name. |
| 11 | `VAL2` | VARCHAR(255) |  |  | Passed in string value 2 to filter scripts. Typically a parameter such as a security attribute. |
| 12 | `VAL3` | VARCHAR(255) |  |  | Passed in string value 3 to filter scripts. Typically a parameter such as a security attribute. |
| 13 | `VAL4` | VARCHAR(255) |  |  | Passed in string value 4 to filter scripts. Typically a parameter such as a security attribute. |
| 14 | `VAL5` | VARCHAR(255) |  |  | Passed in string value 5 to filter scripts. Typically a parameter such as a security attribute. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILTER_MEANING` | [OMF_FILTER_MEANING](OMF_FILTER_MEANING.md) | `FILTER_MEANING` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_AUTH_LOGON_ATTR_RELTN](OMF_AUTH_LOGON_ATTR_RELTN.md) | `OMF_AUTH_ATTR_ID` |

