# MIC_REF_BILLING_PANEL

> This reference table contains a single record for every panel defined on mic_valid_sus_panel. An indicator on the table determines if a charge needs to be sent to billing.

**Description:** Microbiology Reference Billing Panel  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_IND` | DOUBLE | NOT NULL |  | This field includes an indicator documenting whether or not the panel should be billed. |
| 2 | `PANEL_CD` | DOUBLE | NOT NULL |  | If a panel or antibiotic was entered for billing, this field contains the internal identification code assigned to the panel/antibiotic. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VALID_PANEL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to panel billing information stored on the mic_valid_sus_panel reference table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VALID_PANEL_ID` | [MIC_VALID_SUS_PANEL](MIC_VALID_SUS_PANEL.md) | `VALID_PANEL_ID` |

