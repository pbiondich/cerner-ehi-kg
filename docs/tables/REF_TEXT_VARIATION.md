# REF_TEXT_VARIATION

> Stores the reference text to parent_entity relationship. Used to depict different pieces of reference text for a parent_entity

**Description:** Reference Text Variation  
**Table type:** REFERENCE  
**Primary key:** `REF_TEXT_VARIATION_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The id of the entity the text is being associated with, may be an Order Catalog CD or some other id/cd. |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the type of entity you are associating the text too, for example ORDERCATALOG. |
| 3 | `REF_TEXT_NAME` | VARCHAR(100) |  |  | Represents the name of the reference text |
| 4 | `REF_TEXT_VARIATION_ID` | DOUBLE | NOT NULL | PK | The ID of the reference text. Primary key. |
| 5 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL |  | Represents the type of reference text |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [REF_TEXT_FACILITY_R](REF_TEXT_FACILITY_R.md) | `REF_TEXT_VARIATION_ID` |
| [REF_TEXT_VERSION](REF_TEXT_VERSION.md) | `REF_TEXT_VARIATION_ID` |

