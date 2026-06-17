# AP_TAG_GROUP

> This reference table contains the various identification code schemes (the consolidation of multiple tag values) that have been defined for association with a prefix. Examples of schemes might include numeric, alphabetic, and Roman numerals.

**Description:** AP Tag Group  
**Table type:** REFERENCE  
**Primary key:** `TAG_GROUP_ID`  
**Columns:** 7  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `TAG_DESC` | VARCHAR(50) |  |  | This field contains the description associated with the identification scheme. |
| 2 | `TAG_GROUP_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies the row (the identification scheme) included on the AP_TAG_GROUP table. This field would be used to join to other tables (as a foreign key) such as the AP_TAG table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_PREFIX_TAG_GROUP_R](AP_PREFIX_TAG_GROUP_R.md) | `TAG_GROUP_ID` |
| [AP_TAG](AP_TAG.md) | `TAG_GROUP_ID` |

