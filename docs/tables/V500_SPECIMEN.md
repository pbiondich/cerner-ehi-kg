# V500_SPECIMEN

> Every specimen tracked by the PathNet Specimen Collections module will be represented by a row in this table.

**Description:** V500 specimen  
**Table type:** ACTIVITY  
**Primary key:** `SPECIMEN_ID`  
**Columns:** 28  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_SPECIMEN_ID` | DOUBLE | NOT NULL |  | not currently used |
| 2 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Code value identifying the default body site from which this specimen was drawn. |
| 3 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | Code value identifying the collection method used to collect this specimen. |
| 4 | `COLLECTION_MODE` | DOUBLE |  |  | not currently used |
| 5 | `CREATION_DT_TM` | DATETIME | NOT NULL |  | Date and time this specimen was created. |
| 6 | `CREATION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the person who created this entry. |
| 7 | `DRAWN_DT_TM` | DATETIME |  |  | The Date and Time this specimen was collected. |
| 8 | `DRAWN_ID` | DOUBLE | NOT NULL | FK→ | The person id of the individual who collected this specimen. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | not currently being used |
| 10 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The id of the textual specimen source description in the long text table. |
| 11 | `PREV_SPECIMEN_ID` | DOUBLE | NOT NULL |  | Used for tracking when specimens are manipulated in SpecimenLogin. |
| 12 | `QNS_IND` | DOUBLE |  |  | not currently being used |
| 13 | `REJECTION_IND` | DOUBLE |  |  | not currently being used |
| 14 | `REJECTION_REASON_CD` | DOUBLE | NOT NULL |  | not currently being used |
| 15 | `SPECIMEN_COLLECT_PRIORITY_CD` | DOUBLE | NOT NULL |  | Not currently being populated. |
| 16 | `SPECIMEN_COLLECT_VOL` | DOUBLE |  |  | Not currently being used. |
| 17 | `SPECIMEN_COMMENT` | VARCHAR(200) |  |  | Not currently being used. |
| 18 | `SPECIMEN_DANGER_CD` | DOUBLE | NOT NULL |  | Not currently being used. |
| 19 | `SPECIMEN_ID` | DOUBLE | NOT NULL | PK | The system generated number that uniquely identifies each specimen. |
| 20 | `SPECIMEN_SRC_CD` | DOUBLE | NOT NULL |  | not currently being used |
| 21 | `SPECIMEN_SRC_TEXT` | VARCHAR(40) |  |  | Free text specimen source comment. |
| 22 | `SPECIMEN_STATUS_CD` | DOUBLE | NOT NULL |  | not currently being used |
| 23 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | System generated number that uniquely identifies specimen type of the specimen. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DRAWN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BB_SPEC_EXPIRE_OVRD](BB_SPEC_EXPIRE_OVRD.md) | `SPECIMEN_ID` |
| [CE_SPECIMEN_COLL](CE_SPECIMEN_COLL.md) | `SPECIMEN_ID` |
| [CONTAINER](CONTAINER.md) | `SPECIMEN_ID` |
| [CONTAINER_EVENT](CONTAINER_EVENT.md) | `SPECIMEN_ID` |
| [PERSON_ABORH_RESULT](PERSON_ABORH_RESULT.md) | `SPECIMEN_ID` |
| [SPECIMEN_USAGE](SPECIMEN_USAGE.md) | `PARENT_SPECIMEN_ID` |
| [SPECIMEN_USAGE](SPECIMEN_USAGE.md) | `SPECIMEN_ID` |

