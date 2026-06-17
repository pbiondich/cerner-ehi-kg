# HF_OTH_HS_R_TEST_DETAIL

> BLANK

**Description:** HF_OTH_HS_R_TEST_DETAIL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DIRECTION_IND` | DOUBLE |  |  | This indicator specifies which direction to either look back or look forward for the out result relative to the in result. 1 is look back. 2 is look forward. |
| 3 | `ENC_FLG` | DOUBLE |  |  | This lets the rule know if this is person centric or encounter centric. 0 is person and 1 is encounter. |
| 4 | `IN_DETAIL_LAB_PROCEDURE_ID` | DOUBLE | NOT NULL |  | If the look back rule is going to trigger off a general lab test, then the lab_procedure id (from hf_d_lab_procedure) shall be entered. Each rule should only have 1 in_isolate_id or in_detail_lab_procedure_id not both. |
| 5 | `IN_ISOLATE_ID` | DOUBLE | NOT NULL |  | If the look back rule is going to trigger off a microbiology test, then the isolate id (from hf_d_isolate) shall be entered. Each rule should only have 1 in_isolate_id or in_detail_lab_procedure_id not both. |
| 6 | `NUMBER_OF_DAYS` | DOUBLE |  |  | The number of days to look backwards or forwards for the Out test based on the In results. |
| 7 | `OUT_DETAIL_LAB_PROCEDURE_ID` | DOUBLE | NOT NULL |  | This shall contain a lab_procedure_id from hf_d_lab_procedure that the rule will also report if the in_isolate or in_detail_lab_procedure had a reportable result. |
| 8 | `TEST_DETAIL_ID` | DOUBLE | NOT NULL |  | A unique identifier that joins to HF_OTH_HS_R_TEST_RULES for this look back rule. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

