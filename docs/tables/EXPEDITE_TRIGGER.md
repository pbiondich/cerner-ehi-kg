# EXPEDITE_TRIGGER

> Used to determine the conditions to trigger an expedite. These rows are group by name when displayed to the user building the database.

**Description:** Used to determine the conditions to trigger an expedite.  
**Table type:** REFERENCE  
**Primary key:** `EXPEDITE_TRIGGER_ID`  
**Columns:** 38  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Used to define expedites for all procedures of a specific activity type (i.e. blood bank, micro, ...). |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The order catalog item that the expedite rule applies to. Zero indicates that the expedite rule applies to all procedures. |
| 7 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Used to define expedites for all procedures with a specific catalog_type_cd (i.e. lab, radiology, ...). |
| 8 | `CODED_RESP_IND` | DOUBLE |  |  | Indicates the trigger also includes coded responses.Column |
| 9 | `DISCHARGED_FLAG` | DOUBLE |  |  | Indicates whether the discharged/non-discharged status of a patient is used to determine if a result should be expedited. |
| 10 | `EXPEDITE_TRIGGER_ID` | DOUBLE | NOT NULL | PK | Primary key used to uniquely identify the row. Internal system generated number. |
| 11 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Used to specify the location that should trigger an expedite.Column |
| 12 | `LOCATION_CONTEXT_FLAG` | DOUBLE |  |  | Indicates whether the location_cd specified should be used if it is the patient's location, ordering location or temp location. |
| 13 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 14 | `MIC_AFTER_COM_FLAG` | DOUBLE |  |  | Indicates whether expedite the result when any antibiotic is verified/corrected after completion of the susceptibility method |
| 15 | `MIC_COM_FLAG` | DOUBLE |  |  | Indicate whether expedite the result upon completion of the susceptibility method |
| 16 | `MIC_COR_FLAG` | DOUBLE |  |  | Indicate whether expedite the result any antiniotic is correctedColumn |
| 17 | `MIC_VER_FLAG` | DOUBLE |  |  | Indicate whether expedite any antibiotic is verified |
| 18 | `NAME` | VARCHAR(100) | NOT NULL |  | Description of the expedite trigger. Used to group rows together for display purposes in the database building tool. |
| 19 | `NAME_KEY` | VARCHAR(100) | NOT NULL |  | Indexed and converted version of the name column used for searching purposes.Column |
| 20 | `ORDER_COMPLETE_FLAG` | DOUBLE |  |  | If set then the result should only expedite when the order is complete.Column |
| 21 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Organization that should trigger an expedite.Column |
| 22 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | person idColumn |
| 23 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL |  | task that should expedite a PowerForm tirgger |
| 24 | `REPORT_PRIORITY_CD` | DOUBLE | NOT NULL |  | Produce an expedite for a result with this report priority (i.e. routine, stat, ...). Zero indicates that an expedite should be produced for all priorities. |
| 25 | `REPORT_PROCESSING_CD` | DOUBLE | NOT NULL |  | Produce expedites for these events (i.e. first report, final report, ...). Used primarily for micro and Radnet. Zero indicates that an expedite should be produced for all events. |
| 26 | `REPORT_PROCESSING_NBR` | DOUBLE |  |  | Used to indicate the number of times a specific report processing cd should trigger an expedite. |
| 27 | `RESULT_CD` | DOUBLE | NOT NULL |  | Used to indicate the result (i.e. positive or negative) that should trigger an expedite. |
| 28 | `RESULT_NBR` | DOUBLE |  |  | Used to indicate the number of times a particular result (pos or neg) should expedite. |
| 29 | `RESULT_RANGE_CD` | DOUBLE | NOT NULL |  | Used to indicate the result ranges (i.e. high, low, etc.) that should trigger an expedite. |
| 30 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Produce an expedite for a result with this status (i.e. produce an expedite when the result is first performed or every time it is verified...). Zero indicates that an expedite should be produced for all results. |
| 31 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Produce an expedite if the result is performed at this service resource. Zero indicates that an expedite should be produced for all service resources. |
| 32 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | order catalog synonymColumn |
| 33 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Produce an expedite when this task_assay_cd is resulted. Zero indicates that an expedite should be produced for all task_assay_cds. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EXPEDITE_CODED_RESP](EXPEDITE_CODED_RESP.md) | `EXPEDITE_TRIGGER_ID` |
| [EXPEDITE_PARAMS_R](EXPEDITE_PARAMS_R.md) | `EXPEDITE_TRIGGER_ID` |

