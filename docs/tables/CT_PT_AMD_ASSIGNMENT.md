# CT_PT_AMD_ASSIGNMENT

> This table documents the assignment of a patient to an amendment.

**Description:** CT PT AMD ASSIGNMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGN_END_DT_TM` | DATETIME | NOT NULL |  | The date on which the patient's assignment to the amendment ended |
| 2 | `ASSIGN_START_DT_TM` | DATETIME | NOT NULL |  | The date on which the patient was put on this amendment |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CT_PT_AMD_ASSIGNMENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ct_pt_amd_assignment table. It is an internal system assigned number. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | The amendment on which the patient was assigned |
| 7 | `REG_ID` | DOUBLE | NOT NULL |  | Identifies the protocol registration that this assignment is related to. A reg_id is logical identifier in the pt_prot_reg table. It identifier an active enrollment of a patient on a protocol. |
| 8 | `TRANSFER_CHECKED_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | The amendment against which an attempt is done to transfer the patient |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |
| `TRANSFER_CHECKED_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

