from model.appraisal import AppraisalRequest, AppraisalResponse
from util.logging_utils import logger


async def get_appraisal(req: AppraisalRequest) -> AppraisalResponse:
    logger.info(f"Appraisal request: {dict(req)}")
    resp: AppraisalResponse = AppraisalResponse(
        value_range="$12,250 - $13,336", valid=True
    )
    return resp
