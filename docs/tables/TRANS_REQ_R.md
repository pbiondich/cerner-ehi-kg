# TRANS_REQ_R

> A reference of the association between items in the Transfusion Requirements and the special testing items which satisfy the requirements.

**Description:** Transfusion Requirement Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLOW_OVERRIDE_IND` | DOUBLE |  |  | Indicates whether the Dispense application should allow the user to override this transfusion requirement when the product does not have the attribute necessary for this transfusion requirement. An example is the transfusion requirement of the antibody "Kell" on the patient, when the product to be dispensed has not been typed "Kell Negative". |
| 6 | `RELATIONSHIP_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that ensures the uniqueness of each row. |
| 7 | `REQUIREMENT_CD` | DOUBLE | NOT NULL | FK→ | The specific transfusion requirement for which this relationship is defined. Refers to items built on the TRANSFUSION_REQUIREMENT table. |
| 8 | `SPECIAL_TESTING_CD` | DOUBLE | NOT NULL |  | The attribute associated with the transfusion requirement that must be present on the product to be dispensed to a patient with the transfusion requirement defined on this row . These attributes may be red cell antigens or other types of special testing. Examples are "Kell Negative" and "CMV Negative". |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WARN_IND` | DOUBLE |  |  | Indicates whether the user should be warned of this transfusion requirement when it is not met by the product being dispensed. If this indicator is set, then the Dispense application may or may not allow this warning to be overridden depending on the value of the ALLOW_OVERRIDE_IND. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REQUIREMENT_CD` | [TRANSFUSION_REQUIREMENTS](TRANSFUSION_REQUIREMENTS.md) | `REQUIREMENT_CD` |

