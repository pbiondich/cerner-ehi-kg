# LH_CNT_READMIT_STATUS

> This table will contain the statuses of the filters used in the readmission worklist

**Description:** LH_CNT_READMIT_STATUS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_AS_FLAG` | DOUBLE |  |  | Status of the Assessment documentation for this encounter |
| 2 | `DOC_ED_FLAG` | DOUBLE |  |  | Status of the Education documentation for this encounter |
| 3 | `DOC_PP_FLAG` | DOUBLE |  |  | Status of the PowerPlan documentation for this encounter |
| 4 | `FU_DEPART_FLAG` | DOUBLE |  |  | Status of the Follow Up Depart Process documentation for this encounter |
| 5 | `FU_PHONE_DT_TM` | DATETIME |  |  | Contains the date/time of the follow up phone call |
| 6 | `FU_PHONE_FLAG` | DOUBLE |  |  | Status of the Follow Up Phone Call documentation for this encounter |
| 7 | `FU_VISIT_FLAG` | DOUBLE |  |  | Status of the Follow Up Visits documentation for this encounter |
| 8 | `LAST_UPDT_DT_TM` | DATETIME |  |  | This is the last date that the entire table was updated. This will be used to show on the front end how old the data is the end user is reviewing. |
| 9 | `LH_CNT_READMIT_STATUS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_READMIT_STATUS table. |
| 10 | `LH_CNT_READMIT_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | ID of the corresponding row from the LH_CNT_READMIT_WORKLIST table. |
| 11 | `SS_CD1_FLAG` | DOUBLE |  |  | Status of the Support Services Client Defined 1 documentation for this encounter |
| 12 | `SS_CD2_FLAG` | DOUBLE |  |  | Status of the Support Services Home Health documentation for this encounter |
| 13 | `SS_CD3_FLAG` | DOUBLE |  |  | Status of the Support Services Home Health documentation for this encounter |
| 14 | `SS_CM_FLAG` | DOUBLE |  |  | Status of the Support Services Care Management documentation for this encounter |
| 15 | `SS_HC_FLAG` | DOUBLE |  |  | Status of the Support Services Hospice Consult documentation for this encounter |
| 16 | `SS_HH_FLAG` | DOUBLE |  |  | Status of the Support Services Home Health documentation for this encounter |
| 17 | `SS_NC_FLAG` | DOUBLE |  |  | Status of the Support Services Nutrition Consult documentation for this encounter |
| 18 | `SS_OT_FLAG` | DOUBLE |  |  | Status of the Support Services Occ Therapy documentation for this encounter |
| 19 | `SS_PC_FLAG` | DOUBLE |  |  | Status of the Support Services Palliative Care documentation for this encounter |
| 20 | `SS_PT_FLAG` | DOUBLE |  |  | Status of the Support Services Physical Therapy documentation for this encounter |
| 21 | `SS_RC_FLAG` | DOUBLE |  |  | Status of the Support Services Rehab Consult documentation for this encounter |
| 22 | `SS_SS_FLAG` | DOUBLE |  |  | Status of the Support Services Social Services documentation for this encounter |
| 23 | `SS_ST_FLAG` | DOUBLE |  |  | Status of the Support Services Speech Therapy documentation for this encounter |
| 24 | `TR_DC_FLAG` | DOUBLE |  |  | Status of the Transition Readiness Discharge documentation for this encounter |
| 25 | `TR_MED_REC_FLAG` | DOUBLE |  |  | Status of the Transition Readiness Meds Rec documentation for this encounter |
| 26 | `TR_ORDER_FLAG` | DOUBLE |  |  | Status of the Transition Readiness Order documentation for this encounter |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_READMIT_WORKLIST_ID` | [LH_CNT_READMIT_WORKLIST](LH_CNT_READMIT_WORKLIST.md) | `LH_CNT_READMIT_WORKLIST_ID` |

