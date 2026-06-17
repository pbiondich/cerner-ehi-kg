# HANDHELD_CONTAINER

> Handheld Container

**Description:** A single collection (container) uploaded using a handheld device.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | CHAR(20) | NOT NULL |  | This field is the accession number of the uploaded container. |
| 2 | `ALIAS` | VARCHAR(200) |  |  | This field is the alias of the patient for purposes of positive patient identification. |
| 3 | `COLLECTED_DT_TM` | DATETIME | NOT NULL |  | This field contains the collection date and time for the uploaded container. |
| 4 | `COLLECTED_IND` | DOUBLE | NOT NULL |  | This field indicates whether the container was collected or missed. |
| 5 | `COLLECTED_METHOD` | VARCHAR(40) |  |  | This field contains the collection method used to collect the uploaded container. |
| 6 | `COLLECTION_ID` | DOUBLE | NOT NULL |  | This field (with the Report_ID field) uniquely identifies this collection/container. |
| 7 | `COLL_PRIORITY` | VARCHAR(40) |  |  | This field contains the collection priority of the first order in the uploaded container. |
| 8 | `CONTAINER_NUMBER` | DOUBLE | NOT NULL |  | This field contains the accession container number for the uploaded container. |
| 9 | `ERROR_FLAG` | DOUBLE | NOT NULL |  | This field identifies possible error values for the uploaded container/collection. |
| 10 | `OVERRIDE_IND` | DOUBLE | NOT NULL |  | This field indicates whether this container was collected after the user used the HIBC override function. |
| 11 | `PATIENT_NAME` | VARCHAR(100) |  |  | This field contains the name of the patient from which this uploaded container was collected. |
| 12 | `REASON_MISSED` | VARCHAR(40) |  |  | This field contains the reason the uploaded container was missed. |
| 13 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | This field (with the Collection_ID field) uniquely identifies this collection/container. |
| 14 | `REQUESTED_DT_TM` | DATETIME |  |  | This field contains the requested date and time for the first order on an uploaded container. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPORT_ID` | [HANDHELD_REPORT](HANDHELD_REPORT.md) | `REPORT_ID` |

