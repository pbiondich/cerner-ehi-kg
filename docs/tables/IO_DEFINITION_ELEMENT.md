# IO_DEFINITION_ELEMENT

> I&O Total Definition Element

**Description:** Element definition  
**Table type:** REFERENCE  
**Primary key:** `IO_DEFINITION_ELEMENT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code to be used for total calculation |
| 4 | `IO_DEFINITION_ELEMENT_ID` | DOUBLE | NOT NULL | PK | Identifies the primary key for this specific row. |
| 5 | `IV_EVENT_CD` | DOUBLE | NOT NULL |  | Event Set the event code belongs to. |
| 6 | `PREV_IO_DEFINITION_ELEMENT_ID` | DOUBLE | NOT NULL |  | Identifies the original primary key for this row. |
| 7 | `ROUTE_CD` | DOUBLE | NOT NULL |  | Route code to be used for total calculation. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [IO_DEF_ELEMENT_RELTN](IO_DEF_ELEMENT_RELTN.md) | `IO_DEFINITION_ELEMENT_ID` |

