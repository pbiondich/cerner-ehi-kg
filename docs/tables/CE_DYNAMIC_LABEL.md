# CE_DYNAMIC_LABEL

> This table is used to store dynamic label information that will either be related to a group of clinical events or can be stored independently from any clinical events. If a dynamic label is related to a clinical event, this will be signified by the population of the label_id on the clinical_event table.

**Description:** Clinical Event Dynamic Label  
**Table type:** ACTIVITY  
**Primary key:** `CE_DYNAMIC_LABEL_ID`  
**Columns:** 19  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL | PK | Unique, generated primary key for CE_DYNAMIC_LABEL. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the dynamic label was created. |
| 3 | `LABEL_NAME` | VARCHAR(100) |  |  | The name of the label template that was used to create the dynamic label. |
| 4 | `LABEL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the person creating the dynamic_label row. |
| 5 | `LABEL_SEQ_NBR` | DOUBLE | NOT NULL |  | This field identifies the sequence of a label relative to the other labels entered on a patient. The combination of Label_seq and person_id will identify a unique ce_dynamic_label row. |
| 6 | `LABEL_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the dynamic_label. |
| 7 | `LABEL_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | An identifier used to identify the label template that was used to create the dynamic label. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Id of the textual comments associated with this label. |
| 9 | `MODIFIED_IND` | DOUBLE |  |  | Modified Indicator will track whether a dynamic label has been modified. 0 - No. 1 - Yes. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the person that the dynamic label was created for. |
| 11 | `PREV_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique ID of the previous version of the current row. |
| 12 | `RESULT_SET_ID` | DOUBLE | NOT NULL |  | The result_set_id of the group of results that are related to the dynamic label. From table CE_RESULTS_SET_LINK. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VALID_FROM_DT_TM` | DATETIME |  |  | Creation date of the row. |
| 19 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | Date the row becomes historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LABEL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LABEL_TEMPLATE_ID` | [DYNAMIC_LABEL_TEMPLATE](DYNAMIC_LABEL_TEMPLATE.md) | `LABEL_TEMPLATE_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PREV_DYNAMIC_LABEL_ID` | [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `CE_DYNAMIC_LABEL_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `PREV_DYNAMIC_LABEL_ID` |
| [ENCNTR_NEWBORN_CE_RELTN](ENCNTR_NEWBORN_CE_RELTN.md) | `CE_DYNAMIC_LABEL_ID` |
| [LH_CNT_IC_ADV_LTD](LH_CNT_IC_ADV_LTD.md) | `CE_DYNAMIC_LABEL_ID` |
| [LH_CNT_IC_ADV_WOUND_DATA](LH_CNT_IC_ADV_WOUND_DATA.md) | `CE_DYNAMIC_LABEL_ID` |
| [LH_CNT_IC_PATIENT_DEVICE](LH_CNT_IC_PATIENT_DEVICE.md) | `CE_DYNAMIC_LABEL_ID` |
| [LH_CNT_IC_RPT_EVENT](LH_CNT_IC_RPT_EVENT.md) | `CE_DYNAMIC_LABEL_ID` |
| [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `CE_DYNAMIC_LABEL_ID` |

