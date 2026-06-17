# PROT_ARM

> This table stores treatment arm information for an amendment

**Description:** PROT ARM  
**Table type:** REFERENCE  
**Primary key:** `PROT_ARM_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARM_CD` | DOUBLE | NOT NULL |  | This field contains the code for the protocol arm. |
| 2 | `ARM_DESCRIPTION` | VARCHAR(255) |  |  | This field contains a description of the protocol treatment arm. |
| 3 | `ARM_STATUS_CD` | DOUBLE | NOT NULL |  | This field contains a code indicating the status of the protocol arm. The statii include, but are not limited to, open, suspended, closed and terminated |
| 4 | `GROUPWIDE_TARGETED_ACCRUAL` | DOUBLE |  |  | This field contains the targeted accrual for this protocol arm from all institutions enrolling patients in the protocol. |
| 5 | `MOST_RECENT_CLOSURE_SUSP_DT_TM` | DATETIME |  |  | This field contains the date and time of the most recent suspension or closure of the protocol arm. |
| 6 | `PRIMARY_REASON_CLOSURE_SUSP_CD` | DOUBLE | NOT NULL |  | This field contains a code for the primary reason that the protocol arm was suspended or closed. |
| 7 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. This field identifies the protocol amendment for which this treatment arm is defined. |
| 8 | `PROT_ARM_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the prot_arm table. It is an internal system assigned number. |
| 9 | `TARGETED_ACCRUAL` | DOUBLE |  |  | This field contains the targeted number of patients from the coordinating institution to be enrolled in the protocol arm. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PT_PROT_REG](PT_PROT_REG.md) | `PROT_ARM_ID` |

