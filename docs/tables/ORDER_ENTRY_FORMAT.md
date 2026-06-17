# ORDER_ENTRY_FORMAT

> The format that will be associated to an orderable to identify the information to be captured at order time.

**Description:** ORDER ENTRY FORMAT  
**Table type:** REFERENCE  
**Primary key:** `ACTION_TYPE_CD`, `OE_FORMAT_ID`  
**Columns:** 9  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL | PK | The action this format is built for. |
| 2 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog type this format is built for. |
| 3 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | PK | The id for the format. |
| 4 | `OE_FORMAT_NAME` | VARCHAR(200) |  |  | The name of the format. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [OE_FORMAT_FIELDS](OE_FORMAT_FIELDS.md) | `ACTION_TYPE_CD` |
| [OE_FORMAT_FIELDS](OE_FORMAT_FIELDS.md) | `OE_FORMAT_ID` |
| [RLN_SPECIMEN_OEF](RLN_SPECIMEN_OEF.md) | `ACTION_TYPE_CD` |
| [RLN_SPECIMEN_OEF](RLN_SPECIMEN_OEF.md) | `OEF_ID` |

