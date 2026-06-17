# SA_REF_MED_PREFERENCE

> This table will store the default units of measure and various display options to be used for a medication in the anesthesia meds dialog

**Description:** SA Reference Med Preference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BOLUS_DEFAULT_CURSOR_FLAG` | DOUBLE | NOT NULL |  | Displays the dealult cursor location choosen choosen among the options for Bolus2 Weight Based Dose 4 Amount (Default) 5 Volume |
| 3 | `BOLUS_DISPLAY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines what to display for bolus admins |
| 4 | `CONC_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of concentration |
| 5 | `CONC_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for dosage field of concentration |
| 6 | `DEF_ROUTE_CD` | DOUBLE | NOT NULL |  | Stores the default route for a medication. |
| 7 | `DIR_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for dosage in DIR |
| 8 | `DIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time in DIR |
| 9 | `EXCLUDE_IN_TOTAL_VOL_IND` | DOUBLE |  |  | Default Indicator to exclude medication ingredient volume from total concentration volume |
| 10 | `INFUSION_DEFAULT_CURSOR_FLAG` | DOUBLE | NOT NULL |  | Displays the dealult cursor location choosen choosen among the options for Infusion.1 Dosing Infusion Rate (default)2 Weight Based Dose3 Pump Infusion Rate4 Amount Infused5 Volume Infused |
| 11 | `INFUSION_DISPLAY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines what to display for infusions |
| 12 | `PIR_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount in PIR |
| 13 | `PIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time in PIR |
| 14 | `REMINDER_FREQUENCY_MINS` | DOUBLE |  |  | The interval in minutes which represents the default value of frequency of the reminder associated to a medication. |
| 15 | `SA_REF_DOC_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Doc Type Preference Set is tied to |
| 16 | `SA_REF_MEDICATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to sa_ref_medication |
| 17 | `SA_REF_MED_PREFERENCE_ID` | DOUBLE | NOT NULL |  | Primary table identifier |
| 18 | `TOTAL_DISPLAY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines what to display for the total for the medication |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for dosage in WBD |
| 25 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time in WBD |
| 26 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for weight in WBD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_REF_DOC_TYPE_ID` | [SA_REF_DOC_TYPE](SA_REF_DOC_TYPE.md) | `SA_REF_DOC_TYPE_ID` |
| `SA_REF_MEDICATION_ID` | [SA_REF_MEDICATION](SA_REF_MEDICATION.md) | `SA_REF_MEDICATION_ID` |

