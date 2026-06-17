# CDI_AC_FIELD

> This table defines CPDI configurations for Ascent Capture Document Class Fields.

**Description:** cdi ac field  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Person or encounter alias type code. |
| 2 | `ALIAS_TYPE_CODESET` | DOUBLE | NOT NULL |  | Code Set of the Alias_type_cd field. |
| 3 | `AUTO_SEARCH_IND` | DOUBLE | NOT NULL |  | Specifies if the field is required for encounter searching in automatic processing. |
| 4 | `CDI_AC_FIELD_ID` | DOUBLE | NOT NULL |  | Unique ID for the document class field. |
| 5 | `DOC_CLASS_NAME` | VARCHAR(32) | NOT NULL |  | Ascent Capture document class name. |
| 6 | `FIELD_NAME` | VARCHAR(32) | NOT NULL |  | Ascent Capture index field name. |
| 7 | `MANUAL_SEARCH_IND` | DOUBLE | NOT NULL |  | Specifies if the field is required for encounter searching in manual processing. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

