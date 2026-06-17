# MIC_ORDER_LAB

> This table contains the order level activity information for ordered microbiology procedures. Thistable is filled out initially during the order conversation and is updated again when the procedureis received into its performing service resource.

**Description:** Microbiology Orders  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_ID`  
**Columns:** 26  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARCHIVE_DT_TM` | DATETIME |  |  | This field is not used at this time. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 3 | `COMPLETE_DT_TM` | DATETIME |  |  | This field identifies the date and time the procedure was completed. |
| 4 | `CULTURE_START_DT_TM` | DATETIME |  |  | This field identifies the start date and time of the orderable procedure. This field is updated when the procedure is received into its performing service resource. |
| 5 | `DOWNLOAD_IND` | DOUBLE |  |  | This field relates to the blood culture instrument interfaces. Once all of the media associated with a procedure has been successfully downloaded to the instrument this field will be set to 1 indicating that it has downloaded. If not set to 1, user can re-download the procedure again. Valid values include: 1 = downloaded 0 = not downloaded |
| 6 | `EVENT_FLAG` | DOUBLE |  |  | Obsolete. This field is not used at this time. |
| 7 | `INTERP_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the long_text_id value from the long_text table that associates the interpretive data text with this orderable procedure. |
| 8 | `NOSOCOMIAL_IND` | DOUBLE |  |  | Nosocomial refers to an infection that a patient gets while in the hospital. Customization can be done to the number of hours between patient admission and specimen collection that would qualify a culture as a nosocomial infection. So this column indicates when a positive culture is deemed to be an infection that developed while the patient was in the hospital. |
| 9 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 10 | `ORDER_LOCK_DT_TM` | DATETIME |  |  | This field identifies the date and time the record was locked. When the user exits the microbiology application accessing the accession this field will be set to null. |
| 11 | `ORDER_LOCK_ID` | DOUBLE | NOT NULL |  | This field identifies the id of the person that currently has this order_id locked. The order_lock_id corresponds to the person_id on the prsnl table, which identifies the user. When the user exits the microbiology application accessing the accession this field will be set to null. |
| 12 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether or not the procedure is considered positive. Microbiology procedures are considered positive when a preliminary or final report is issued that includes a positive response or organism. Valid values include: 0 = Not positive 1 = Positive |
| 13 | `PRELIMINARY_POSITIVE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 14 | `PURGE_DT_TM` | DATETIME |  |  | This field is not used at this time. |
| 15 | `REPORT_IND` | DOUBLE |  |  | This field indicates whether or not a report has been issued for the procedure. This indicator is used by the microbiology inquiry application to quickly identify if a procedure has a report issued.Valid values include: 0 = No report issued 1 = Report has been issued. |
| 16 | `RESTORED_DT_TM` | DATETIME |  |  | This field is not used at this time. |
| 17 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Identifies the service_resource code_value (code set 221 service resource) for the orderable procedure. This is the service resource code where the procedure is currently located and where interpretive data text will be extracted from for this procedure. This field is only filled out if there is interpretive data associated with the orderable procedure. |
| 18 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the current status of the orderable procedure. The status code_value is fromcode set 1031 & 1905 Micro Status. |
| 19 | `SUSCEPTIBILITY_IND` | DOUBLE |  |  | This field indicates whether or not a susceptibility has been ordered for the procedure. This indicator is used by the microbiology inquiry application to quickly identify if a procedure has a susceptibility ordered. Valid values include: 0 = No susceptibilities ordered 1 = Susceptibilities ordered |
| 20 | `SUS_INSTR_ID_NBR` | CHAR(18) |  |  | This field is not used at this time. |
| 21 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Identifies the task_assay_cd from the discrete_task_assay code set(14003) for the orderable procedure. This field is only filled out if there is interpretive data associated with the orderable procedure. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `INTERP_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `ORDER_ID` |
| [MIC_ANG_AUTOMATED](MIC_ANG_AUTOMATED.md) | `ORDER_ID` |
| [MIC_MEDIA_ACTIVITY](MIC_MEDIA_ACTIVITY.md) | `ORDER_ID` |
| [MIC_MEDS_ACTIVITY](MIC_MEDS_ACTIVITY.md) | `ORDER_ID` |
| [MIC_PATHOGEN](MIC_PATHOGEN.md) | `ORDER_ID` |
| [MIC_REQUIRED_TASK](MIC_REQUIRED_TASK.md) | `ORDER_ID` |

