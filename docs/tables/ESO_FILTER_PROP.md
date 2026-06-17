# ESO_FILTER_PROP

> eso filter property Table

**Description:** eso filter property  
**Table type:** REFERENCE  
**Primary key:** `FILTER_PROP_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date that the record was created in the table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FILTER_ID` | DOUBLE | NOT NULL | FK→ | filter identifierColumn |
| 6 | `FILTER_PROP_CD` | DOUBLE | NOT NULL |  | filter property codeColumn |
| 7 | `FILTER_PROP_ID` | DOUBLE | NOT NULL | PK | filter property identifierColumn |
| 8 | `FILTER_PROP_VALUE` | VARCHAR(255) |  |  | filter property valueColumn |
| 9 | `ORIGINAL_FILTER_PROP_IDENT` | DOUBLE | NOT NULL |  | original filter property identifierColumn |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILTER_ID` | [ESO_FILTER](ESO_FILTER.md) | `FILTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ESO_FILTER_PROP_ATTRIB](ESO_FILTER_PROP_ATTRIB.md) | `FILTER_PROP_ID` |

