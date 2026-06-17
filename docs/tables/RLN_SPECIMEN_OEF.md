# RLN_SPECIMEN_OEF

> This table will store the relationship between specimen types and order entry formats for each connected partner lab.

**Description:** Reference Lab Network - Specimen Order Entry Format  
**Table type:** REFERENCE  
**Primary key:** `RLN_SPECIMEN_OEF_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_CLASS_CD` | DOUBLE | NOT NULL |  | The accession class associated with the specimen type. |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The action this format is built for. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | The collection method associated with a specimen type. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `OEF_ID` | DOUBLE | NOT NULL | FK→ | Along with the action_type_cd, uniquely identifies the related order entry format. |
| 8 | `ORIG_RLN_SPECIMEN_OEF_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the specimen and order entry format information. This field will always point back to the original value created. This may be used to find the correct version when combined with the begin and end effective dates and times |
| 9 | `RLN_CONTRIBUTOR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related contributor. |
| 10 | `RLN_SPECIMEN_OEF_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a relationship between a specimen type and an order entry format for a given partner lab. |
| 11 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of specimen |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_TYPE_CD` | [ORDER_ENTRY_FORMAT](ORDER_ENTRY_FORMAT.md) | `ACTION_TYPE_CD` |
| `OEF_ID` | [ORDER_ENTRY_FORMAT](ORDER_ENTRY_FORMAT.md) | `OE_FORMAT_ID` |
| `ORIG_RLN_SPECIMEN_OEF_ID` | [RLN_SPECIMEN_OEF](RLN_SPECIMEN_OEF.md) | `RLN_SPECIMEN_OEF_ID` |
| `RLN_CONTRIBUTOR_ID` | [RLN_CONTRIBUTOR](RLN_CONTRIBUTOR.md) | `RLN_CONTRIBUTOR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RLN_SPECIMEN_OEF](RLN_SPECIMEN_OEF.md) | `ORIG_RLN_SPECIMEN_OEF_ID` |

