# CYTO_SCREENING_SECURITY

> This reference table contains user-specific parameters with regards to required rescreening percentages (and associated parameters) and a verification security level associated with cytology reports.

**Description:** Cytology Screening Security  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_PERCENTAGE` | DOUBLE |  |  | This field documents the % of gyn cytology cases associated with patients with abnormal gyn history (from the total of those cases that could have been verified by the user based on verification security) that will be selected for required rescreening. |
| 2 | `ABNORMAL_REQUEUE_FLAG` | DOUBLE |  |  | This field contains a flag value indicating whether or not requeueing will be invoked for cases selected for required rescreening based on a previous abnormal flag. If invoked, this flag documents whether the requeueing is manual or automatic. |
| 3 | `ABNORMAL_REQUEUE_RANK` | DOUBLE |  |  | This field documents the ranking associated with the previous abnormal flag. This ranking determines which flag (if multiple are present for the patient) takes precedence when evaluating whether or not required rescreening should be invoked. |
| 4 | `ABNORMAL_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field documents the service resource which should be used during the requeueing process. The association of a service resource with requeueing parameters is optional based on the requeue flag specified. |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ATYPICAL_PERCENTAGE` | DOUBLE |  |  | This field documents the % of gyn cytology cases associated with patients with atypical gyn history (from the total of those cases that could have been verified by the user based on verification security) that will be selected for required rescreening. |
| 7 | `ATYPICAL_REQUEUE_FLAG` | DOUBLE |  |  | This field contains a flag value indicating whether or not requeueing will be invoked for cases selected for required rescreening based on a previous atypical flag. If invoked, this flag documents whether the requeueing is manual or automatic. |
| 8 | `ATYPICAL_REQUEUE_RANK` | DOUBLE |  |  | This field documents the ranking associated with the previous atypical flag. This ranking determines which flag (if multiple are present for the patient) takes precedence when evaluating whether or not required rescreening should be invoked. |
| 9 | `ATYPICAL_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field documents the service resource which should be used during the requeueing process. The association of a service resource with requeueing parameters is optional based on the requeue flag specified. |
| 10 | `AUTO_OVERSCREENER_IND` | DOUBLE |  |  | This field is not used at this time. |
| 11 | `CHR_PERCENTAGE` | DOUBLE |  |  | This field documents the % of gyn cases associated with patients flagged as clinically high risk (from the total of those cases that could have been verified by the user based on verification security) that will be selected for required rescreening. |
| 12 | `CHR_REQUEUE_FLAG` | DOUBLE |  |  | This field contains a flag value indicating whether or not requeueing will be invoked for cases selected for required rescreening based on a high risk flag. If invoked, this flag documents whether the requeueing is manual or automatic. |
| 13 | `CHR_REQUEUE_RANK` | DOUBLE |  |  | This field documents the ranking associated with the high risk flag. This ranking determines which flag (if multiple are present for the patient) takes precedence when evaluating whether or not required rescreening should be invoked. |
| 14 | `CHR_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field documents the service resource which should be used during the requeueing process. The association of a service resource with requeueing parameters is optional based on the requeue flag specified. |
| 15 | `COMMENTS` | VARCHAR(200) |  |  | This field contains any comments entered when a cytotechnologist's screening security was reviewed. |
| 16 | `NORMAL_PERCENTAGE` | DOUBLE |  |  | This field documents the % of gyn cases associated with patients with normal or no gyn history (from the total of those cases that could have been verified by the user based on verification security) that will be selected for required rescreening. |
| 17 | `NORMAL_REQUEUE_FLAG` | DOUBLE |  |  | This field contains a flag value indicating whether or not requeueing will be invoked for cases selected for required rescreening based on a previous normal flag. If invoked, this flag documents whether the requeueing is manual or automatic. |
| 18 | `NORMAL_REQUEUE_RANK` | DOUBLE |  |  | This field documents the ranking associated with the previous normal flag. This ranking determines which flag (if multiple are present for the patient) takes precedence when evaluating whether or not required rescreening should be invoked. |
| 19 | `NORMAL_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field documents the service resource which should be used during the requeueing process. The association of a service resource with requeueing parameters is optional based on the requeue flag specified. |
| 20 | `OVER_REQUEUE_FLAG` | DOUBLE |  |  | This field is not used at this time. |
| 21 | `OVER_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field is not used at this time. |
| 22 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies the cytotechnologist for whom screening security has been defined or reviewed. This value could be used to join to other tables, such as the PRSNL, PERSON, and CYTO_SCREENING_LIMITS, for example. |
| 23 | `REVIEWED_DT_TM` | DATETIME |  |  | This field contains the date the time the review event occurred. |
| 24 | `REVIEWER_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the user who is documented as the reviewer for the cytotechnologist's screening security and requeueing parameters. This ID could be used to join to the PRSNL or PERSON tables. |
| 25 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field documents the record sequence available for the cytotechnologist. The initial limit definition would be represented as the first sequence, the first review would be represented as the second sequence, etc. |
| 26 | `UNSAT_PERCENTAGE` | DOUBLE |  |  | This field documents the % of gyn cases with a diagnosis of unsatisfactory that will be selected for required rescreening. |
| 27 | `UNSAT_REQUEUE_FLAG` | DOUBLE |  |  | This field contains a flag value indicating whether or not requeueing will be invoked for cases selected for required rescreening based on a unsatisfactory flag. If invoked, this flag documents whether the requeueing is manual or automatic. |
| 28 | `UNSAT_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field documents the service resource which should be used during the requeueing process. The association of a service resource with requeueing parameters is optional based on the requeue flag specified. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 34 | `VERIFY_LEVEL` | DOUBLE |  |  | This field documents the verification level, specific for the verification of cytology reports, that has been established for the cytotechnologist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ABNORMAL_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `ATYPICAL_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `CHR_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `NORMAL_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `OVER_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `UNSAT_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

