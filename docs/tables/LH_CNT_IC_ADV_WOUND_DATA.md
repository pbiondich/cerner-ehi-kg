# LH_CNT_IC_ADV_WOUND_DATA

> Custom table for Infection Control Advisor that will store Incision/Wound data that has been saved by the user.

**Description:** LH_CNT_IC_ADV_WOUND_DATA  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMALITY_TYPE_DISP` | VARCHAR(250) |  |  | Display string for the documented Abnormality Type. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CE_DYNAMIC_LABEL_ID` | DOUBLE | NOT NULL | FK→ | The label_id of the dynamic label that this Incision/Wound is associated with. (from ce_dynamic_label.label_id) |
| 5 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the EKS_ADVSR_EVENT table |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the ENCOUNTER table |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EVENT_DT_TM` | DATETIME |  |  | The date time that the Incision/Wound event occurred. |
| 9 | `EXUDATE_DISP` | VARCHAR(250) |  |  | Display string for the documented Exudate. |
| 10 | `INC_WOUND_DISP` | VARCHAR(250) |  |  | The Incision/Wound display label. Concatenation of Laterality, Location Description, and Location. |
| 11 | `LH_CNT_IC_ADV_WOUND_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_ADV_WOUND_DATA table. |
| 12 | `SURGICAL_INC_WOUND_IND` | DOUBLE | NOT NULL |  | Indicator to designate 'Surgical' or 'Other' Incision/Wounds. 0 = Other, 1 = Surgical |
| 13 | `TISSUE_COLOR_DISP` | VARCHAR(250) |  |  | Display string for the documented Tissue Color. |
| 14 | `TISSUE_CONDITION_DISP` | VARCHAR(250) |  |  | Display string for the documented Tissue Condition. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_DYNAMIC_LABEL_ID` | [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `CE_DYNAMIC_LABEL_ID` |
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

