# PROCESSING_TASK

> This activity table contains records for processing tasks ordered for current pathology cases. Parameters specific to the processing tasks, and their status, are included.

**Description:** Processing Task  
**Table type:** ACTIVITY  
**Primary key:** `PROCESSING_TASK_ID`  
**Columns:** 39  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CANCEL_CD` | DOUBLE | NOT NULL |  | If the processing task is cancelled, this field contains the identification code associated with the cancellation reason. |
| 2 | `CANCEL_DT_TM` | DATETIME |  |  | If the processing task is cancelled, this field contains the date and time the cancellation event occurred. |
| 3 | `CANCEL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | If the processing task is cancelled, this field contains the internal identification code of the user who executed the cancellation event. This value could be used to join to user information stored on the PRSNL and PERSON tables. |
| 4 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 5 | `CASE_SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to specimen information stored on the CASE_SPECIMEN table. This field represents the specimen to which the processing task is associated. |
| 6 | `CASE_SPECIMEN_TAG_ID` | DOUBLE | NOT NULL |  | This field contains an identifier referencing the identification code assigned to the specimen to which this processing task is associated. |
| 7 | `CASSETTE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to block/cassette information stored on the CASSETTE table. This field represents the block/cassette to which the processing task is associated. |
| 8 | `CASSETTE_TAG_ID` | DOUBLE | NOT NULL |  | This field contains an identifier referencing the identification code assigned to the block/cassette to which this processing task is associated. |
| 9 | `COMMENTS` | VARCHAR(500) |  |  | This field in no longer used. Refer to the COMMENTS_LONG_TEXT_ID for information regarding the processing ORDER COMMENT. |
| 10 | `COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the order comment. |
| 11 | `CREATE_INVENTORY_FLAG` | DOUBLE |  |  | This field contains a numeric flag value indicating whether or not the completion of the associated processing task (discrete task) causes one or more pathology inventory records to be created. |
| 12 | `HOLD_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 13 | `HOLD_COMMENT` | VARCHAR(100) |  |  | This field is not used at this time. |
| 14 | `HOLD_COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field is not used at this time. |
| 15 | `HOLD_DT_TM` | DATETIME |  |  | This field is not used at this time. |
| 16 | `HOLD_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field is not used at this time. |
| 17 | `LABEL_PRINTED_IND` | DOUBLE |  |  | This field contains an indicator documenting whether or not slide labels have been printed for the associated task. |
| 18 | `NO_CHARGE_IND` | DOUBLE | NOT NULL |  | This field indicates whether the processing task is a 'no charge' task. |
| 19 | `ORDER_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key value used to join to order information stored on the ORDERS table. |
| 20 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | This field contains the priority code value associated with the processing task. |
| 21 | `PROCESSING_TASK_ID` | DOUBLE | NOT NULL | PK | This field uniquely defines a row included on the PROCESSING_TASK table. This field represents a specific processing task order. |
| 22 | `QUANTITY` | DOUBLE |  |  | This field is not used at this time. |
| 23 | `QUEUE_ID` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 24 | `REQUEST_DT_TM` | DATETIME |  |  | This field contains the date and time the processing task was ordered. |
| 25 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the user who ordered the processing task. This value could be used to join to user information stored on the PRSNL and PERSON tables. |
| 26 | `RESEARCH_ACCOUNT_ID` | DOUBLE | NOT NULL |  | This field contains the internal ID code of the research acccount associated with the processing task. |
| 27 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal id code of the service resource to which the task is assigned. This could be used to join to the service_resource table. |
| 28 | `SLIDE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value (representing the slide to which the processing task is associated) used to join to slide information stored on the SLIDE table. |
| 29 | `SLIDE_TAG_ID` | DOUBLE | NOT NULL |  | This field contains an identifier referencing the identification code assigned to the slide to which this processing task is associated. |
| 30 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the internal ID code of the status associated with the processing task. Valid statuses include options such as ordered, verified, and cancelled. |
| 31 | `STATUS_DT_TM` | DATETIME |  |  | This field includes the date and time the processing task achieved the status documented in the STATUS_CD field. |
| 32 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field includes the internal identification code associated with the user who caused the task to be updated to the status documented in the STATUS_CD field. This could be used to join to personnel information on the PRSNL or PERSON tables. |
| 33 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the discrete task for which this processing task is associated. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `WORKLIST_NBR` | DOUBLE |  |  | This field includes the worklist batch number, if assigned, associated with the processing task. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CANCEL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `CASE_SPECIMEN_ID` | [CASE_SPECIMEN](CASE_SPECIMEN.md) | `CASE_SPECIMEN_ID` |
| `CASSETTE_ID` | [CASSETTE](CASSETTE.md) | `CASSETTE_ID` |
| `COMMENTS_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `HOLD_COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `HOLD_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REQUEST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SLIDE_ID` | [SLIDE](SLIDE.md) | `SLIDE_ID` |
| `STATUS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TASK_INSTRMT_PROTCL_R](TASK_INSTRMT_PROTCL_R.md) | `PROCESSING_TASK_ID` |

