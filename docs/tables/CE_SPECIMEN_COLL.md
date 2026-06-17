# CE_SPECIMEN_COLL

> The ce_specimen_coll table contains information abouit the physical specimen upon which an event was performed. A specimen record can only be associated with a root event. For a group event, all detail events must be on the same specimen.

**Description:** ce specimen coll  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Body location where the collection was done (left arm, right thumb, etc.). |
| 2 | `COLLECT_DT_TM` | DATETIME | NOT NULL |  | Date and time of the collection. |
| 3 | `COLLECT_LOC_CD` | DOUBLE | NOT NULL |  | Patient¿s location when the specimen was collected. |
| 4 | `COLLECT_METHOD_CD` | DOUBLE | NOT NULL |  | Collection method (venous, arterial, etc.) (Is this the same as code set 2053 ¿ Collection Route?) |
| 5 | `COLLECT_PRIORITY_CD` | DOUBLE | NOT NULL |  | Collection priority. |
| 6 | `COLLECT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identification number of the clinician who collected the specimen. |
| 7 | `COLLECT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 8 | `COLLECT_UNIT_CD` | DOUBLE | NOT NULL |  | Unit code of the collection volume. |
| 9 | `COLLECT_VOLUME` | DOUBLE | NOT NULL |  | Collection volume and unit specify the amount of collection |
| 10 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | Foreign key to Container Table. |
| 11 | `CONTAINER_TYPE_CD` | DOUBLE | NOT NULL |  | Type of container (purple top, red top, AP pail, etc.). |
| 12 | `DANGER_CD` | DOUBLE | NOT NULL |  | Code or text indicating any known or suspected patient or specimen hazards. |
| 13 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Event Table. |
| 14 | `POSITIVE_IND` | DOUBLE | NOT NULL |  | Foreign key to the Event Table. |
| 15 | `RECVD_DT_TM` | DATETIME |  |  | The date and time the specimen is received into the lab that will be processing it. |
| 16 | `RECVD_TZ` | DOUBLE |  |  | The time zone of the user who received the specimen in the lab that will be processing it. |
| 17 | `SOURCE_TEXT` | VARCHAR(255) |  |  | Free-text source. |
| 18 | `SOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | Source of collection (blood, sputum, stool, etc.) |
| 19 | `SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Specimen Table. Foreign Key: XFK2 - (v500 specimen) |
| 20 | `SPECIMEN_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the specimen (collected, transfer, received, etc.). |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the "Beginning Point" of when a row in the table is valid. |
| 27 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLLECT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SPECIMEN_ID` | [V500_SPECIMEN](V500_SPECIMEN.md) | `SPECIMEN_ID` |

