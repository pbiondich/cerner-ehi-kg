# TASK_SUBACTIVITY

> This table is used to store the relationship between action requests and their associated tasks.

**Description:** Action Requests and Task Relationships  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_REQUEST_CD` | DOUBLE | NOT NULL |  | CODESET 3400 This field identifies the action requested by the user. |
| 2 | `IB_RX_REQ_ID` | DOUBLE | NOT NULL | FK→ | The inbound Rx Request, from the IB_RX_REQ table, that the task is linked to. |
| 3 | `MEDIA_IDENT` | VARCHAR(255) |  |  | The identifier of the attached media. |
| 4 | `MEDIA_NAME` | VARCHAR(255) |  |  | The name of the attached media at the time the notification was created. |
| 5 | `MEDIA_VERSION_NBR` | DOUBLE |  |  | The version of the attached media at the time the notification was created. |
| 6 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | The order_proposal_id, from the order_proposal table, that the task is linked to. |
| 7 | `PATHWAY_NOTIFICATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of a plan phase which will be populated for a plan phase accept or reject receipt. |
| 8 | `PORTAL_USER_UUID` | VARCHAR(128) |  |  | Identifier of a HealtheLife patient portal user account that is allowed access to the notification about the patient. This user may be the patient or a proxy user that is allowed access to the patient's information such as a parent, guardian, or spouse. |
| 9 | `PROPOSAL_ACTION_FLAG` | DOUBLE | NOT NULL |  | Illustrates the action that was taken on the order proposal. Valid flag values are: 1 - Accepted, 2 - Rejected, 3 - Withdrawn |
| 10 | `PROPOSAL_ACTION_REASON_CD` | DOUBLE | NOT NULL |  | The codified reason that is supplied by the user to communicate the order proposal action. |
| 11 | `PROPOSAL_ACTION_REASON_TXT` | VARCHAR(1000) |  |  | The free text reason that is supplied by the user to communicate details of the order proposal action. |
| 12 | `RECEIPT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The indication of the type of receipt. 0 -not valued, 1 - Accepted, 2 - Rejected |
| 13 | `REFERRAL_ID` | DOUBLE |  | FK→ | Identifier of a referral that is linked to the notification |
| 14 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:CARENET_SEQ a unique identifier used to associate the action request to the task. |
| 15 | `TASK_SUBACTIVITY_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:CARENET_SEQ a unique, generated number that is used to identify an individual subactivity task |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IB_RX_REQ_ID` | [IB_RX_REQ](IB_RX_REQ.md) | `IB_RX_REQ_ID` |
| `ORDER_PROPOSAL_ID` | [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_PROPOSAL_ID` |
| `PATHWAY_NOTIFICATION_ID` | [PATHWAY_NOTIFICATION](PATHWAY_NOTIFICATION.md) | `PATHWAY_NOTIFICATION_ID` |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |

