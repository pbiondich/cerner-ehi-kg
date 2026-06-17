# RX_WF_WS

> Contains activity data with Worksheet information for Workflow events.

**Description:** Pharmacy Workflow Worksheet  
**Table type:** ACTIVITY  
**Primary key:** `RX_WF_WS_ID`  
**Columns:** 48  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_LABOR_COST_AMT` | DOUBLE | NOT NULL |  | The labor cost required to actually create the product. |
| 2 | `ACTUAL_LABOR_NBR` | DOUBLE | NOT NULL |  | The amount of time required to create the product. |
| 3 | `ASSEMBLE_DT_TM` | DATETIME |  |  | Date/time the manufacturing process began. |
| 4 | `ASSEMBLE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person who began the manufacturing process. |
| 5 | `ASSEMBLE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with ASSEMBLE_DT_TM. |
| 6 | `CHECKED_DT_TM` | DATETIME |  |  | Date/time that a verification that the assembly included everything was performed. |
| 7 | `CHECKED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person who performed the verification that the assembly included everything. |
| 8 | `CHECKED_TZ` | DOUBLE | NOT NULL |  | Time Zone associated with CHECKED_DT_TM. |
| 9 | `EXP_DT_TM` | DATETIME |  |  | The date/time the product will expire. (production date + stability information) |
| 10 | `EXP_TZ` | DOUBLE | NOT NULL |  | Time Zone associated with EXP_DT_TM. |
| 11 | `FINAL_CHK_DT_TM` | DATETIME |  |  | Date/time of the last check of the worksheet before actual creation of the product. |
| 12 | `FINAL_CHK_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person who performed the last check of the worksheet before actual creation of the product. |
| 13 | `FINAL_CHK_TZ` | DOUBLE | NOT NULL |  | Time zone associated with FINAL_CHK_DT_TM. |
| 14 | `FINAL_PROD_CHK_DT_TM` | DATETIME |  |  | Date/time of the very last check of the created product. |
| 15 | `FINAL_PROD_CHK_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person that performed the very last check of the created product. |
| 16 | `FINAL_PROD_CHK_TZ` | DOUBLE | NOT NULL |  | Time zone associated with FINAL_PROD_CHK_DT_TM. |
| 17 | `MANF_DT_TM` | DATETIME |  |  | Date/time of the completion of the creation of the product using the ingredients and instructions on the worksheet. |
| 18 | `MANF_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person who completed the creation of the product using the ingredients and instructions on the worksheet. |
| 19 | `MANF_TZ` | DOUBLE | NOT NULL |  | Time zone associated with MANF_DT_TM. |
| 20 | `MIXING_INSTR_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Instructions for the manufacturing of the product. |
| 21 | `PREPARE_QTY` | DOUBLE | NOT NULL |  | The quantity of product to prepare to satisfy the requirements of this worksheet. Calculated by (charge qty / product dispense qty) * dispense doses |
| 22 | `PRODUCTION_DT_TM` | DATETIME |  |  | Date/time the manufacturing process began. |
| 23 | `PRODUCTION_TZ` | DOUBLE | NOT NULL |  | Time zone associated with PRODUCTION_DT_TM. |
| 24 | `QC_APPROVED_DT_TM` | DATETIME |  |  | Date/time the Quality Control function indicated that the created product was correct. |
| 25 | `QC_APPROVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that performing the Quality Control function that indicated that the created product was correct. |
| 26 | `QC_APPROVED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with QC_APPROVED_DT_TM. |
| 27 | `QC_RECONCILE_DT_TM` | DATETIME |  |  | Date and time that person doing the quality control process signs off on their role. |
| 28 | `QC_RECONCILE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person that signs off on the quality control process. |
| 29 | `QC_RECONCILE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with QC_RECONCILE_DT_TM. |
| 30 | `QC_SAMPLE_AMT` | DOUBLE | NOT NULL |  | The amount of the product in the quality control sample. |
| 31 | `QC_SAMPLE_FORM_CD` | DOUBLE | NOT NULL |  | The form of the product supplied in the quality control sample. |
| 32 | `QC_SAMPLE_NBR` | DOUBLE | NOT NULL |  | The size of the quality control sample. |
| 33 | `QC_SAMPLE_RELEASED_AMT` | DOUBLE | NOT NULL |  | The number of quality control samples released for use. |
| 34 | `QC_SAMPLE_TXT` | VARCHAR(255) | NOT NULL |  | The Quality Control notes created as a result of examining the samples. |
| 35 | `QC_SAMPLE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure of the quality control sample. |
| 36 | `REJECTED_DOSE_NBR` | DOUBLE | NOT NULL |  | The number of doses rejected and/or wasted. |
| 37 | `RX_WF_WS_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_WF_WS table. |
| 38 | `RX_WORKFLOW_STS_ID` | DOUBLE | NOT NULL | FK→ | The workflow associated to this worksheet. |
| 39 | `RX_WS_FAC_RELTN_HX_ID` | DOUBLE | NOT NULL | FK→ | FK to the RX_WS_FAC_RELTN_HX table. This is the worksheet that this workflow implemented. |
| 40 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Status of worksheet. 0 = not completed, 1 = Completed. |
| 41 | `TOTAL_COST_AMT` | DOUBLE | NOT NULL |  | The total cost of the product including item costs and labor costs. |
| 42 | `TOTAL_ITEM_COST_AMT` | DOUBLE | NOT NULL |  | The total cost of the product only counting the cost of the items. |
| 43 | `TOTAL_RELEASED_DOSE_NBR` | DOUBLE | NOT NULL |  | The number of doses released after quality control has been completed. (Total_dose_nbr - rejected_dose_nbr) |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 47 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSEMBLE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CHECKED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FINAL_CHK_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FINAL_PROD_CHK_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `MANF_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `MIXING_INSTR_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `QC_APPROVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `QC_RECONCILE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RX_WORKFLOW_STS_ID` | [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `RX_WORKFLOW_STS_ID` |
| `RX_WS_FAC_RELTN_HX_ID` | [RX_WS_FAC_RELTN_HX](RX_WS_FAC_RELTN_HX.md) | `RX_WS_FAC_RELTN_HX_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_WF_WS_ITEM_RELTN](RX_WF_WS_ITEM_RELTN.md) | `RX_WF_WS_ID` |

