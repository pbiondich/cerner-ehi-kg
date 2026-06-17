# RAD_REPORT_DETAIL

> The Rad_Report_Detail table contains information about each of the report sections that make up a radiology report.

**Description:** Rad Report Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACR_CODE_IND` | DOUBLE |  |  | The ACR_Code_Ind indicates if an ACR code has been assigned. |
| 2 | `DETAIL_EVENT_ID` | DOUBLE | NOT NULL |  | The Detail_Event_Id is a foreign key to the Clinical_Event table. It identifies the report section that is stored in the repository. |
| 3 | `DETAIL_REFERENCE_NBR` | VARCHAR(40) |  |  | The Detail_Reference_Nbr serves as a tie to the Clinical_Event row that represents one of the report sections. |
| 4 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The Rad_Report_Id is a foreign key to the Rad_Report table. It identifies the report that the report detail belongs to. |
| 5 | `REQUIRED_IND` | DOUBLE |  |  | The Required_Ind indicates whether or not the report section is required. |
| 6 | `SECTION_SEQUENCE` | DOUBLE | NOT NULL |  | The Section_Sequence indicates in what order the report sections should appear. |
| 7 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The Task_Assay_Cd is a foreign key to the Discrete_Task_Assay table. It identifies the report detail. |
| 8 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The Template_Id is a foreign key to the WP_Template table. It identifies the template that was used for this report section. If one was used at all. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

